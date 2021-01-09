Vue.component('film-list', {
  props: ['filmData', 'imageBase'],
  template: `
        <div>
            <ul v-if="filmData" class="collapsible">
            <li v-for="movie in filmData" v-bind:key="movie.id">
                <div class="collapsible-header">{{movie.title}}</div>
                <div class="collapsible-body">
                <div class="row">
                    <div class="col s12 m4 l2">
                    <img class="materialboxed responsive-img" src="{{imageBase}}{{movie.poster_path}}">
                    </div>
                    <div class="col s12 m8 l4">
                    <h4>{{ movie.title }}</h4>
                    <h5>Overview</h5>
                    <p>{{ movie.overview }}</p>
                    <h5>Release Date</h5>
                    <p>{{ movie.release_date}}</p>
                    </div>
                    <div class="col s12 m12 l6">
                        <canvas id="trend-{{ movie.id }}"></canvas>
                    </div>
                </div>
                </div>
            </li>
            </ul>
            <p v-else>
            Empty
            </p>
        </div>
        `
});